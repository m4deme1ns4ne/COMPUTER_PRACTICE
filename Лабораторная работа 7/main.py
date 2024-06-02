from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from PIL import Image, ImageDraw
import io
import base64

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/makeimage", response_class=HTMLResponse)
async def get_make_image(request: Request):
    return templates.TemplateResponse("makeimage.html", {"request": request, "message": ""})

@app.post("/makeimage")
async def post_make_image(request: Request, width: int = Form(...), height: int = Form(...), text: str = Form(...)):
    if width <= 0 or height <= 0:
        return templates.TemplateResponse("makeimage.html", {"request": request, "message": "Invalid image size"})

    image = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, fill="black")

    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return templates.TemplateResponse("displayimage.html", {"request": request, "image_data": img_str})

@app.get("/login")
async def login():
    return JSONResponse(content={"author": "1141531"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
