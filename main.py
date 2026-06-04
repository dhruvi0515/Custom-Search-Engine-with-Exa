from exa_py import Exa
exa=Exa('YOUR_EXA_API_KEY')
query=input('Search Here')
response=exa.search(
  query,
  num_results=10,
  type='keyword',
    )
print('\n -------Search Results------')
for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()
