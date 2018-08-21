curl https://localhost:8443/swagger.json -o swagger.json --insecure
cp ../cli/dist/swagger.json proxy-swagger.json

swagger-codegen generate -c config.json -i ./swagger.json -o erc_dex -l python
swagger-codegen generate -c proxy-config.json -i ./proxy-swagger.json -o erc_dex_proxy -l python