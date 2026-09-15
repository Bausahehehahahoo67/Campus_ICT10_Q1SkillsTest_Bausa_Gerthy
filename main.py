from pyscript import document, display

def create_order(e): 
    

def create_order2(e):
    milo = document.getElementById('Finale receipt').innerHTML = "" #clears previous
    milo = document.getElementById('milo')
    milo_value = float(milo.value)
    display(f"Your order costs: ${milo_value:.2f}", target = 'Finale receipt')