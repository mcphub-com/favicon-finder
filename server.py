import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/JSPMedia/api/favicon-finder'

mcp = FastMCP('favicon-finder')

@mcp.tool()
def favicon_url(url: Annotated[str, Field(description='Enter a valid URL starting with the http:// or https:// protocols.')],
                fallback: Annotated[Union[str, None], Field(description='Enter a fallback URL in favicon_url if no favicon is found.')] = None) -> dict: 
    '''Get the favicon URL of any web page.'''
    url = 'https://faviconfinder.p.rapidapi.com/faviconurl/'
    headers = {'x-rapidapi-host': 'faviconfinder.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
        'fallback': fallback,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
