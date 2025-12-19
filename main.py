from fastapi import FastAPI


app = FastAPI(title="Air Travel")


@app.get("/")
async def main():
    return "Air Travel Service"
