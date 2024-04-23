import requests # Biblioteca pra requisições HTTP
import json

url_base = 'https://api.xdr.trendmicro.com'
url_path = '/beta/xdr/threatintel/suspiciousObjects' # Caminho para o endpoint da API da Trend
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJjaWQiOiJkZmU2MmRkMi1jNDhiLTRkM2ItODFkYi05NzZkMDM1MWUzMTkiLCJjcGlkIjoic3ZwIiwicHBpZCI6ImN1cyIsIml0IjoxNzEzNzk5NzgyLCJldCI6MjE4NjgzOTc4MSwiaWQiOiJhNDZlNGM1OS03YTdlLTQyOGMtYjA3YS00YmFlYjViNjFlYzAiLCJ0b2tlblVzZSI6ImN1c3RvbWVyIn0.pUhU6ZWZ3-bSucPfDCqYBcFeKEjQ-p9MWGNnRd3xHV3LXpZ79wnQk5mgdiUF7AoxVy1-cEJVss-_Jy0f0j2-LqiU3vFbDMVK0LjspXry8qkUPOKtNdpI0YyABOHEnJouMs3HK6kAmYWLy6KG77RpH4UnVhyMjuCllATWeSCID6Oru8JCAijfjcxtEC5uUoKvFfkiH8OJZZnlXJiuT81OBvH9H1DD7az0ILnCniYjEHf_tP5rJS5h2FylCMIe0jDb8bXnD6zN49qYLqkZhmKv6LSFhUZVY0otwX2AXpbqJOv9jN-ecH_jFUnVacJpK7nnEqGwPgYHSbBB9G0r--jym2pnakJphRi3n9fMm5FQOuICLpnYa9i3PdSK9bF45NZsvbBVMvuJoaOkx07M56Q1j8IonfzZ-7tclkR-YHVgAqj3SoaKO_7TerubLrPcmX8fXyhuQY6V_vx0_8Ib-RlBUKQomGwX-6nMnDY8coOYjQs2KIlKpcd6rmROWStIBb4XYlxqs7tNmFx7yedvsWSZbB6Xw2zNT59VWK3YAmmOqGGthj-Zd4tIdPPa2b_jMLukXKNhlgGMnIu8Yu5as_FOXOMYsnN6zVG_4UCg7aBLtGn80hNCYqXUNpf4vbo9e4PnMeKHh0mNpU9SixRQ_rXFWQmn19I6SBnlD_AJAHzQvJc'

query_params = {
    # Parâmetros abaixo:
    'orderBy': 'YOUR_ORDERBY (string)' , # informações de ordenação: 
    'startDateTime': 'startDateTime=2021-04-05T08:22:37Z', # Desde quando serão inseridos os IOCs: 
    'endDateTime': 'YOUR_ENDDATETIME (string)', # Até quando serão inseridos os IOcs: 
    'top': 'YOUR_TOP (integer)' # Número de registros exibidos em uma página: 
}
headers = {
    'Authorization': 'Bearer ' + token, # Tipo de autorização
    'TMV1-Filter': "type eq 'ip' AND riskLevel eq 'high'" # Filtros aplicados. Aqui, só serão escolhidos IPs com risco alto
}

# Get feito usando os parâmetros que passamos acima
r = requests.get(url_base + url_path, params=query_params, headers=headers)

# Print das requisições encontradas no Suspect Object Management/Workbench
print(f"Erro: {r.status_code}")
for key, value in r.headers.items():
    print(f"Dicionário: {key}: {value}")
print('')
if 'application/json' in r.headers.get('Content-Type', '') and len(r.content):
    print(json.dumps(r.json(), indent=4))
else:
    print(r.text)