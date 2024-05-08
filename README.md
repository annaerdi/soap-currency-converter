commands used for azure deployment:

```
az webapp up --resource-group ResourceGroupName --plan AppServicePlan --name AppName --runtime PYTHON:3.8 --logs
```

or to set up new resource group and plan, just without those flags:
```
az webapp up --runtime PYTHON:3.8 --sku B1 --logs
```

set which python file to run for starting the service:
```
az webapp config set --resource-group MyResourceGroup --name MyPythonApp --startup-file "python main.py"
```
