async function fetchData() {
    try {
        const response = await fetch('/get_uid_data'); // Gọi API Flask
        const data = await response.json();

        if (data.status === "success") {
            updateTable(data.table);
        } else {
            console.log("No data available");
        }
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

function updateTable(tableData) {
    const tableBody = document.getElementById('table-body');
    tableBody.innerHTML = ""; // Xóa dữ liệu cũ

    tableData.forEach(row => {
        const tr = document.createElement('tr');
        row.forEach(cell => {
            const td = document.createElement('td');
            td.textContent = cell;
            tr.appendChild(td);
        });
        tableBody.appendChild(tr);
    });
}

// Cập nhật bảng mỗi 5 giây
setInterval(fetchData, 5000);

// Gọi fetch lần đầu
fetchData();