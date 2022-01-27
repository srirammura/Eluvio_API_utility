# Eluvio_API_utility

# Problem Statement

Imagine you have a program that needs to look up information about items using their item ID, often in large batches.

Unfortunately, the only API available for returning this data takes one item at a time, which means you will have to perform one query per item. Additionally, the API is limited to five simultaneous requests. Any additional requests will be served with HTTP 429 (too many requests).

Write a client utility for your program to use that will retrieve the information for all given IDs as quickly as possible without triggering the simultaneous requests limit, and without performing unnecessary queries for item IDs that have already been seen.

API Usage:

GET https://challenges.qluv.io/items/:id

Required headers:

Authorization: Base64(:id)

Example:

curl https://challenges.qluv.io/items/cRF2dvDZQsmu37WGgK6MTcL7XjH -H "Authorization: Y1JGMmR2RFpRc211MzdXR2dLNk1UY0w3WGpI"

# Solution

- I have used Python ThreadPoolExecutor to execute parallel threads to a max of 5, after 5 it creates a new parallel thread and so on.
- To deal with repetition of ids and I have lru_cache (least recently used cache ) from the functools library

# Performance Results 

| Name      | No.of ID's | Description            | Total time taken  |
|-----------|------------|------------------------|-------------------|
| test1.txt | 10         | No repetition of ids   | 4.64 seconds      |
| test2.txt | 50         | High repetition of ids | 6.45 seconds      |
| test3.txt | 80         | Low repetition         | 18.9 seconds      |
| test4.txt | 100        | Medium repetition      | 19.72 seconds     |
| test5.txt | 150        | Medium repetition      | 21.95 seconds     |

