// function external() {
//     alert("External JS");
// }

// let calc = function(num1, num2, calcType) {
//     if (calcType === "add") {
//         return num1 + num2;
//     } else if (calcType === "multiply") {
//         return num2 * num1;
//     } else {

//         return num1 / num2;
//     }
// }
// console.log(calc(4, 5, "multiply"));

var data = [{ "page": 1, "pages": 1, "per_page": "50", "total": 1 },
    [{
        "id": "AFG",
        "iso2Code": "AF",
        "name": "Afghanistan",
        "region": { "id": "SAS", "iso2code": "8S", "value": "South Asia" },
        "adminregion": { "id": "SAS", "iso2code": "8S", "value": "South Asia" },
        "incomeLevel": { "id": "LIC", "iso2code": "XM", "value": "Low income" },
        "lendingType": { "id": "IDX", "iso2code": "XI", "value": "IDA" },
        "capitalCity": "Kabul",
        "longitude": "69.1761",
        "latitude": "34.5228"
    }]
];

for (let p in data) {
    //productName would be "laptop", "cellphone", etc.
    //products[productName] would be an array of brand/price objects
    var inner = data[p];
    for (var i = 0; i < inner.length; i++) {
        console.log(inner[i].id);
        console.log(inner[i].name);
    }
}