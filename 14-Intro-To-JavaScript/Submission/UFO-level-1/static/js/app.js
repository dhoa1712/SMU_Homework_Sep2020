// from data.js
var tableData = data;

// YOUR CODE HERE!

$(document).ready(function() {
    console.log("page loaded");
    builtTable()
    $("#filter-btn").on("click", function(e) {
        e.preventDefault();
        builtTable();
    });

    $("#form").on("submit", function(e) {
        e.preventDefault();
        builtTable();
    });
});

function builtTable() {
    var dateInput = $("#datetime").val();
    if (dateInput === "") {
        builtTableString(data);
    } else {
        var filteredData = tableData.filter(row => row.datetime === dateInput);
        if (filteredData.length === 0) {
            alert("There is no data from chosen date")
        };
        builtTableString(filteredData);
    }
}


function builtTableString(data) {

    var tbody = $("#ufo-table>tbody");
    tbody.empty();
    data.forEach(function(row) {
        var newRow = "<tr>"
        Object.entries(row).forEach(function([key, value]) {
            newRow += `<td>${value}</td>`
        });
        newRow += "</tr>";
        tbody.append(newRow);
    });
}