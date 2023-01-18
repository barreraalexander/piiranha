from pydantic import BaseModel, constr, conint
from typing import Optional, List
from datetime import datetime

# !!! SCHEMAS FOR GENERAL USE !!!
class AuthenticationObject(BaseModel):
    acctId: int
    key: str

class BaseRequestObject(BaseModel):
    serviceId: str
    apiVer: str
    auth: str
    sageNum: int




# !!! SCHEMAS FOR PRODUCT DATA !!!
class product_data_update_Sizes(BaseModel):
    val: Optional[str]
    units: Optional[int]
    type: Optional[int]

class product_data_update_Pics(BaseModel):
    url: Optional[str]
    data: Optional[str]
    caption: Optional[str]
    hasLogo: Optional[bool]

class product_data_update_Value(BaseModel):
    url: Optional[str]
    data: Optional[str]
    caption: Optional[str]
    hasLogo: Optional[bool]


class product_data_update_Options(BaseModel):
    name: str
    values: Optional[product_data_update_Value]
    # pricingIsTotal: Optional[bool]
    pricingIsTotal: Optional[conint(strict=True)]
    # priceCode: Optional[str(constr)]
    priceCode: Optional[constr(max_length=10)]



class product_data_update_Quantity(BaseModel):
    pass

class product_data_update_Currency(BaseModel):
    pass


class product_data_update_Product(BaseModel):
    updateType: int
    refNum: str
    productId: int
    suppId: int
    itemNum: str
    name: Optional[str]
    cat1Id: Optional[int]
    cat1Name: Optional[str]
    cat2Id: Optional[int]
    cat2Name: Optional[str]
    page1: Optional[str]
    page2: Optional[str]
    description: Optional[str]
    keywords: Optional[List[str]]
    colors: Optional[List[str]]
    themes: Optional[List[str]]
    sizes: Optional[List[product_data_update_Sizes]]
    quantities: Optional[List[product_data_update_Quantity]]
    prices: Optional[List[product_data_update_Currency]]
    prCode: Optional[str]
    piecesPerUnit: Optional[List[int]] = [1]
    quoteUponRequest: Optional[bool] = False
    priceIncludesClr: str
    priceIncludesSide: str
    priceIncludesLoc: str
    options: Optional[List[str]]
    # additionalCharges: Add




# !!! SCHEMAS FOR ORDER STATUS !!!


class order_status_update_CustomerRec(BaseModel):
    acctNum: constr(max_length=25)
    company: Optional[constr(max_length=200)]
    phone: Optional[constr(max_length=25)]
    

class order_status_update_ShipmentRec(BaseModel):
    packageId: Optional[int]
    shipDate: datetime
    carrier: constr(max_length=5)
    trackingNum: constr(max_length=25)




class order_status_update_StatusRec(BaseModel):
    timeStamp: Optional[datetime] = datetime.utcnow()
    internalId: Optional[constr(max_length=25)]
    customer: order_status_update_CustomerRec
    orderNum: constr(max_length=25)
    poNum: constr(max_length=25)
    sageOrderId: Optional[int]
    statusId: int #if the status name is provided, this field is optional
    statusName: constr(max_length=25)
    comments: Optional[constr(max_length=25)]
    responseRequired: bool


class order_status_update_Request(AuthenticationObject, BaseRequestObject):
    statusPackets: List[order_status_update_StatusRec]
    # pass
    # pass


