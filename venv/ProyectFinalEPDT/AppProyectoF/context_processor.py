
def total_carrito(request) :
    total = 0
    numeroItems = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += float(value["acumulado"])
                numeroItems = numeroItems +1
    return {"total_carrito": total,"total_items": numeroItems }

