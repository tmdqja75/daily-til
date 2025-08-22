from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "FlightBooking",
    instructions="You are a helpful assistant that can help with flight booking.",
    host="0.0.0.0",
    port=8001
)

@mcp.tool()
def get_flight_info(country: str) -> dict:
    """
    Get flight information for a given country.

    This function returns a list of flight information for the given country.

    Args:
        country (str): The country to get flight information for.

    Returns:
        dict: The flight information for the given country.
    """
    flight_info = {
        {"airport": "ICN",
        "flight_number": "ABC123",
        "flight_to": "LAX"},
        {"airport": "ICN",
        "flight_number": "DEF456",
        "flight_to": "NRT"},
        {"airport": "ICN",
        "flight_number": "GHI789",
        "flight_to": "HNL"},
    }
    return flight_info


if __name__ == "__main__":
    mcp.run(transport="sse")