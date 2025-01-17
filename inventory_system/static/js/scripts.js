// Simple JS to enhance interactivity

// Confirm before deleting an item (example for delete operations)
function confirmDelete(message = "Are you sure you want to delete this item?") {
    return confirm(message);
}

// Highlight table row on hover
document.addEventListener("DOMContentLoaded", function () {
    const rows = document.querySelectorAll("table tbody tr");
    rows.forEach(row => {
        row.addEventListener("mouseover", () => {
            row.style.backgroundColor = "#ffe5e5";
        });
        row.addEventListener("mouseout", () => {
            row.style.backgroundColor = "";
        });
    });
});
