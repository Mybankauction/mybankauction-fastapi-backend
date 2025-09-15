from beanie import Document
from typing import Optional,Any
from pydantic import Field
from datetime import datetime

from pydantic.v1 import BaseSettings


class Property(Document):
    _id : Any
    account_name: str = Field(alias="Account name")
    auction_id: str = Field(alias="Auction Id")
    bank_name: str = Field(alias="Bank Name")
    emd: str = Field(alias="EMD")
    branch_name: str = Field(alias="Branch Name")
    service_provider: str = Field(alias="Service Provider")
    reserve_price: Any = Field(alias="Reserve Price")
    contact_details: str = Field(alias="Contact Details")
    description: str = Field(alias="Description")
    state: str = Field(alias="State")
    city: str = Field(alias="City")
    area: str = Field(alias="Area")
    borrower_name: str = Field(alias="Borrower Name")
    property_type: str = Field(alias="Property Type")
    auction_type: str = Field(alias="Auction Type")
    sub_end: str = Field(alias="Sub End")
    sale_notice: str = Field(alias="sale_notice")
    asset_category: Optional[str] = Field(default=None,alias="AssetCategory")
    outstanding_amount: Any = Field(alias="outstanding_amount")
    auction_start_date: Any = Field(alias="auction_start_date")
    auction_end_date: Any = Field(alias="auction_end_date")

    class Settings:
        name = "Eauctionindia"