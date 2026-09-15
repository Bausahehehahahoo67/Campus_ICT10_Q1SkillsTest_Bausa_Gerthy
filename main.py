from pyscript import document, display

def create_order(e):
    document.getElementById("Subtotal").innerHTML = "" # clears previous output
    document.getElementById("VAT TAX").innerHTML = ""
    document.getElementById("Total Amount").innerHTML = ""

    coffee = document.getElementById('Coffee')
    coffeeprice = float(coffee.value) * coffee.checked

    icedmilo = document.getElementById('Iced Milo')
    icedmiloprice = float(icedmilo.value) * icedmilo.checked

    milk = document.getElementById('Milk')
    milkprice = float(milk.value) * milk.checked

    mocha = document.getElementById('Mocha')
    mochaprice = float(mocha.value) * mocha.checked

    macchiato = document.getElementById('Macchiato')
    macchiatoprice = float(macchiato.value) * macchiato.checked

    subtotal = coffeeprice + icedmiloprice + milkprice + mochaprice + macchiatoprice
    vat = subtotal * 0.12
    total = vat + subtotal


    Sub = f"Subtotal: ₱{subtotal:.2f}"
    display(Sub, target = "Subtotal")

    Vat = f"VAT: ₱{vat:.2f}"
    display(Vat, target = "VAT TAX")

    Total = f"Total: ₱{total:.2f}"
    display(Total, target = "Total Amount")