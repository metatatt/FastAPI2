from fastapi import FastAPI

from py3dbp import Packer, Bin, Item

app = FastAPI()

@app.get("/")
async def root():
    packer = Packer()
    packer.add_bin(Bin('medium-box', 30, 22, 15, 970.0))
    packer.add_bin(Bin('large-box', 38, 27, 15, 970.0))
    packer.add_item(Item('50g [powder 1]', 5, 29, 14, 1))
    packer.add_item(Item('50g [powder 2]', 29, 15, 15, 2))

    packer.pack()

    response1 = ""
    response2 = ""

    for b in packer.bins:
        response1 = b.string()

        response2 = "<br>FITTED："
        for item in b.items:
            response2 += item.string()

        response2 += "<br>UNFITTED："
        for item in b.unfitted_items:
            response2 += item.string()

        response2 += "<br>*************"

    return {"bin": response1, "items": response2}
