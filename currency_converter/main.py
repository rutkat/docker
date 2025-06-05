# Tutorial Docker instructions from current directory
#
# -Build the Docker image:
# docker build -t currency-api .
#
# -Run the container
# docker run -p 8000:8000 currency-api
#
# Test the endpoint with curl
# curl "http://localhost:8000/convert?amount=25&from_currency=EUR&to_currency=USD"
#

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Literal

app = FastAPI(title="Currency Converter")


class ConversionResponse(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    converted: float
    rate: float


mock_rates = {
    ("USD", "EUR"): 0.91,
    ("EUR", "USD"): 1.10,
    ("USD", "JPY"): 145.0,
}

@app.get("/convert", response_model=ConversionResponse)
def convert(
    amount: float = Query(..., gt=0),
    from_currency: Literal["USD", "EUR"] = "USD",
    to_currency: Literal["USD", "EUR", "JPY"] = "EUR",
):
    if from_currency == to_currency:
        raise HTTPException(
            status_code=400, detail="Currency types must be different."
        )

    rate = mock_rates.get((from_currency, to_currency))
    if not rate:
        raise HTTPException(status_code=400, detail="Rate unavailable.")

    converted = amount * rate
    return ConversionResponse(
        from_currency=from_currency,
        to_currency=to_currency,
        amount=amount,
        converted=round(converted, 2),
        rate=rate,
    )
