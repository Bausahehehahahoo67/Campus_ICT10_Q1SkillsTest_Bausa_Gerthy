from pyscript import document, display

def create_order(e):
    document.getElementById("Subtotal").innerHTML = "" # clears previous output
    document.getElementById("VAT TAX").innerHTML = ""
    document.getElementById("Total Amount").innerHTML = ""

    item1 = document.getElementById('Coffee')
    price1 = float(item1.value) * item1.checked

    item2 = document.getElementById('Iced Milo')
    price2 = float(item2.value) * item2.checked

    item3 = document.getElementById('Milk')
    price3 = float(item3.value) * item3.checked

    item4 = document.getElementById('Mocha')
    price4 = float(item4.value) * item4.checked

    item5 = document.getElementById('Macchiato')
    price5 = float(item5.value) * item5.checked

    subtotal = price1 + price2 + price3 + price4 + price5
    tax = subtotal * 0.12
    total = tax + subtotal


    Sub = f"Subtotal: ₱{subtotal:.2f}"
    display(Sub, target = "Subtotal")

    Vat = f"Tax: ₱{tax:.2f}"
    display(Vat, target = "VAT TAX")

    Total = f"Total: ₱{total:.2f}"
    display(Total, target = "Total Amount")