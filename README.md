## Configuracion basica para que funcionen los notebooks en jupyter

Create a `.env` file at the root and add the following variables:

```
OPENAI_API_KEY=<your-key>

LANGCHAIN_API_KEY=<your-key>
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT="<your-project-name>"
```