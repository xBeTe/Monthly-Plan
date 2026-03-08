import sys
import base64
import urllib.request
import os

def render_mermaid(mermaid_text, output_file):
    # Encode the mermaid code to base64
    graph_bytes = mermaid_text.encode('utf-8')
    base64_bytes = base64.b64encode(graph_bytes)
    base64_string = base64_bytes.decode('utf-8')
    
    # URL for mermaid.ink API which returns image
    url = f"https://mermaid.ink/img/{base64_string}"
    
    try:
        print(f"Downloading image from {url} ...")
        # Add a custom User-Agent, as some APIs block default Python urllib agents
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(output_file, 'wb') as f:
                f.write(response.read())
        print(f"Success: Mermaid chart rendered and saved to {output_file}")
    except Exception as e:
        print(f"Failed to render mermaid chart: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python render_mermaid.py <input.mmd> <output.png>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        sys.exit(1)
        
    with open(input_file, 'r', encoding='utf-8') as f:
        mermaid_text = f.read()
        
    render_mermaid(mermaid_text, output_file)
