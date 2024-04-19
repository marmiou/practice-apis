## Comparison of HTTP Requests

| Method   | Description                                       | Idempotent?    | Safe?      | Body        | Example Usage                                         |
|----------|---------------------------------------------------|----------------|------------|-------------|-------------------------------------------------------|
| GET      | Retrieve data from a server                       | Yes            | Yes        | No          | Fetching a webpage, retrieving resource information   |
| POST     | Send data to be processed to a specified resource | No             | No         | Yes         | Submitting form data, creating a new resource         |
| PUT      | Update or replace data on a server                | Yes            | No         | Yes         | Updating an existing resource, uploading a file       |
| PATCH    | Partially update data on a server                 | No             | No         | Yes         | Modifying specific fields of an existing resource     |
| DELETE   | Delete data from a server                        | Yes            | No         | No          | Removing a resource, deleting a file                  |
| HEAD     | Retrieve metadata from a server                   | Yes            | Yes        | No          | Checking resource headers without fetching content   |
| OPTIONS  | Retrieve the supported HTTP methods for a resource| Yes            | Yes        | No          | Discovering available operations for a resource       |


## Mandatory & Optional Attributes

| Method   | Request Attributes                             | Response Attributes                            |
|----------|-------------------------------------------------|-----------------------------------------------|
| GET      | Path parameters (optional)                      | Resource representation                       |
|          | Query parameters (optional)                     | Metadata (headers)                            |
|----------|-------------------------------------------------|-----------------------------------------------|
| POST     | Request body (mandatory)                       | Status code indicating success or failure     |
|          | Path parameters (optional)                      | Resource representation (optional)            |
|----------|-------------------------------------------------|-----------------------------------------------|
| PUT      | Request body (mandatory, entire resource)      | Status code indicating success or failure     |
|          | Path parameters (mandatory)                    | Resource representation (optional)            |
|----------|-------------------------------------------------|-----------------------------------------------|
| PATCH    | Request body (mandatory, partial updates)      | Status code indicating success or failure     |
|          | Path parameters (mandatory)                    | Modified data (response body)                 |
|----------|-------------------------------------------------|-----------------------------------------------|
| DELETE   | Path parameters (mandatory)                    | Status code indicating success or failure     |
|----------|-------------------------------------------------|-----------------------------------------------|
| HEAD     | Path parameters (optional)                      | Metadata (headers)                            |
|----------|-------------------------------------------------|-----------------------------------------------|
| OPTIONS  | Path parameters (optional)                      | Supported HTTP methods (response body)        |


## Status Codes
### HTTP Status Codes:

#### 1xx - Informational
| Status Code | Description                  |
|-------------|------------------------------|
| 100         | Continue                     |
| 101         | Switching Protocols          |
| 102         | Processing (WebDAV)          |
| 103         | Early Hints                  |

#### 2xx - Success
| Status Code | Description                  |
|-------------|------------------------------|
| 200         | OK                           |
| 201         | Created                      |
| 202         | Accepted                     |
| 203         | Non-Authoritative Information|
| 204         | No Content                   |
| 205         | Reset Content                |
| 206         | Partial Content              |
| 207         | Multi-Status (WebDAV)        |
| 208         | Already Reported (WebDAV)    |
| 226         | IM Used (RFC 3229)           |

#### 3xx - Redirection
| Status Code | Description                  |
|-------------|------------------------------|
| 300         | Multiple Choices             |
| 301         | Moved Permanently            |
| 302         | Found                        |
| 303         | See Other                    |
| 304         | Not Modified                 |
| 305         | Use Proxy                    |
| 307         | Temporary Redirect           |
| 308         | Permanent Redirect           |

#### 4xx - Client Errors
| Status Code | Description                  |
|-------------|------------------------------|
| 400         | Bad Request                  |
| 401         | Unauthorized                 |
| 402         | Payment Required             |
| 403         | Forbidden                    |
| 404         | Not Found                    |
| 405         | Method Not Allowed           |
| 406         | Not Acceptable               |
| 407         | Proxy Authentication Required|
| 408         | Request Timeout              |
| 409         | Conflict                     |
| 410         | Gone                         |
| 411         | Length Required              |
| 412         | Precondition Failed          |
| 413         | Payload Too Large            |
| 414         | URI Too Long                 |
| 415         | Unsupported Media Type       |
| 416         | Range Not Satisfiable        |
| 417         | Expectation Failed           |
| 418         | I'm a teapot (RFC 2324)     |
| 421         | Misdirected Request          |
| 422         | Unprocessable Entity         |
| 423         | Locked                       |
| 424         | Failed Dependency            |
| 425         | Too Early                    |
| 426         | Upgrade Required             |
| 428         | Precondition Required        |
| 429         | Too Many Requests            |
| 431         | Request Header Fields Too Large|
| 451         | Unavailable For Legal Reasons|

#### 5xx - Server Errors
| Status Code | Description                  |
|-------------|------------------------------|
| 500         | Internal Server Error        |
| 501         | Not Implemented              |
| 502         | Bad Gateway                  |
| 503         | Service Unavailable          |
| 504         | Gateway Timeout              |
| 505         | HTTP Version Not Supported   |
| 506         | Variant Also Negotiates      |
| 507         | Insufficient Storage         |
| 508         | Loop Detected                |
| 510         | Not Extended                 |
| 511         | Network Authentication Required|
