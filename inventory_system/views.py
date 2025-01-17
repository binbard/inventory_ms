from django.shortcuts import render, redirect
from .models import Product, Supplier, SaleOrder, StockMovement
from .forms import ProductForm, StockMovementForm, SupplierForm, SaleOrderForm
from django.contrib import messages
from django.db.models import Sum

def home(request):
    return redirect("list_products")

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            add_stock_movement(request, product)
            return redirect("list_products")
    else:
        form = ProductForm()
    return render(request, "inventory/add_product.html", {"form": form})

def list_products(request):
    products = Product.objects.select_related('supplier').all()
    return render(request, "inventory/list_products.html", {"products": products})

def add_supplier(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_suppliers")
    else:
        form = SupplierForm()
    return render(request, "inventory/add_supplier.html", {"form": form})

def list_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, "inventory/list_suppliers.html", {"suppliers": suppliers})

def add_stock_movement(request, product: Product):
    if request.method == "POST":
        stock_movement = StockMovement(
                product=product,
                quantity=product.stock_quantity,
                movement_type="In",
                notes="Initial stock added upon product creation"
            )
        stock_movement.save()

def create_sale_order(request):
    if request.method == "POST":
        form = SaleOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_sale_orders')
    else:
        form = SaleOrderForm()
    return render(request, 'inventory/create_sale_order.html', {'form': form})

def update_sale_order_status(request, order_id):
    order = SaleOrder.objects.get(id=order_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')

        if new_status in ['Pending', 'Completed', 'Cancelled']:
            order.status = new_status
            order.save()

            if new_status == 'Completed':
                stock_movement = StockMovement(
                    product=order.product,
                    quantity=-order.quantity,
                    movement_type='Out',
                    notes=f'Sale order {order_id} completed'
                )
                stock_movement.save()
            elif new_status == 'Cancelled':
                stock_movement = StockMovement(
                    product=order.product,
                    quantity=order.quantity,
                    movement_type='In',
                    notes=f'Sale order {order_id} cancelled'
                )
                stock_movement.save()

            messages.success(request, f"Sale order status updated to {new_status}.")
        else:
            messages.error(request, "Invalid status.")

    return redirect('list_sale_orders')

def cancel_sale_order(request, pk):
    sale_order = SaleOrder.objects.get(pk=pk)
    sale_order.status = "Cancelled"
    sale_order.save()
    return redirect("list_sale_orders")

def complete_sale_order(request, pk):
    sale_order = SaleOrder.objects.get(pk=pk)
    sale_order.status = "Completed"
    sale_order.save()
    return redirect("list_sale_orders")

def list_sale_orders(request):
    sale_orders = SaleOrder.objects.all()
    return render(request, "inventory/list_sale_orders.html", {"sale_orders": sale_orders})

def stock_level_check(request):
    products = Product.objects.all()
    low_stock_products = [product for product in products if product.stock_quantity < 10]
    return render(request, "inventory/stock_level_check.html", {"low_stock_products": low_stock_products})

def stock_movements(request):
    stock_movements = StockMovement.objects.all()
    products = Product.objects.all()
    stock_level = None
    selected_product = None

    if 'product' in request.GET:
        product_id = request.GET['product']
        selected_product = Product.objects.get(id=product_id)

        stock_in = StockMovement.objects.filter(product=selected_product, movement_type='In').aggregate(Sum('quantity'))['quantity__sum'] or 0
        stock_out = StockMovement.objects.filter(product=selected_product, movement_type='Out').aggregate(Sum('quantity'))['quantity__sum'] or 0
        stock_level = max(0,stock_in+stock_out)

    return render(request, 'inventory/stock_movements.html', {
        'stock_movements': stock_movements,
        'products': products,
        'stock_level': stock_level,
        'selected_product': selected_product
    })