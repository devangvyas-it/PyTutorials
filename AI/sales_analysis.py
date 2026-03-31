import pandas as pd
from google import genai
import time

start_time = time.time()
client = genai.Client(api_key='your-api-key')
print(f"Client creation completed in {round(time.time() - start_time, 2)}")

start_time = time.time()

# load Excel file and get data string
df = pd.read_excel("sales_data.xlsx")
data_text = df.to_string()

prompt = f"""
Analyze this sales dataset and provide insights.

Data:
{data_text}

Provide:
1. Top selling product
2. Best performing region
3. Any trend you notice
"""

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

print(f"Analysis completed in {round(time.time() - start_time, 2)}")
print(response.text)

# Save the response to a Markdown file
with open("sales_analysis.md", "w", encoding="utf-8") as f:
    f.write(response.text)
    
print("\n[INFO] Data successfully written to sales_analysis.md")