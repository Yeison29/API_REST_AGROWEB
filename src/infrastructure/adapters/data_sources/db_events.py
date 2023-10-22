from src.aplications.app import ap


@ap.app.on_event("startup")
async def startup():
    await ap.startup()


@ap.app.on_event("shutdown")
async def shutdown():
    await ap.disconnect()
