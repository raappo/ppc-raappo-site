import os

# Configuration
BASE_DIR = "public"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
DOMAIN = "ppc.raappo.cf"
PAGE_COUNT = 110

# Create directories
os.makedirs(DOCS_DIR, exist_ok=True)

# Sample technical topics to make the site look high-value
topics = [
    "Quantum-Safe CSS Architectures", "Agentic Workflows in Python 3.14", 
    "Edge-Native Database Sharding", "Sub-millisecond Real-time Rendering",
    "Post-Quantum Encryption for WebSockets", "Neural-Interface API Standards",
    "Hyper-local Mesh Networking protocols", "Autonomous DevOps Pipelines"
]

def generate_page(id):
    topic = topics[id % len(topics)]
    filename = f"tech-guide-{id}.html"
    filepath = os.path.join(DOCS_DIR, filename)
    
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{topic} - Chapter {id}</title>
    <style>body{{font-family:sans-serif; line-height:1.6; max-width:800px; margin:40px auto; padding:0 20px; color:#333;}} a{{color:#0070f3;}}</style>
</head>
<body>
    <nav><a href="/">← Home</a></nav>
    <h1>{topic}: Advanced Implementation Chapter {id}</h1>
    <section>
        <h2>Overview of {topic}</h2>
        <p>In the evolving landscape of 2026 technology, {topic} represents a paradigm shift in how we approach distributed systems. This chapter explores the nuances of Chapter {id} and its implications for modern developers.</p>
        <p>The integration of {topic} into existing stacks requires a deep understanding of low-latency protocols and decentralized verification methods.</p>
    </section>
    <section>
        <h2>Technical Deep Dive</h2>
        <p>Implementing {topic} at scale involves addressing the constraints of sub-millisecond execution. Data suggests that by optimizing the transport layer, we can achieve 40% higher throughput.</p>
        <p>Security remains a primary concern. Utilizing hardware-level abstraction layers ensures that {topic} remains resilient against adversarial AI-driven attacks common in the current cycle.</p>
    </section>
    <footer>
        <hr>
        <p><a href="tech-guide-{id+1}.html">Read Next: Chapter {id+1} →</a></p>
    </footer>
</body>
</html>"""
    
    with open(filepath, "w") as f:
        f.write(content)
    return filename, topic

print(f"🚀 Generating {PAGE_COUNT} pages...")

pages = []
for i in range(1, PAGE_COUNT + 1):
    fname, title = generate_page(i)
    pages.append((fname, title))

# 1. Generate index.html
index_content = f"""<!DOCTYPE html>
<html>
<head><title>2026 Tech Encyclopedia</title><style>body{{font-family:sans-serif; max-width:800px; margin:40px auto;}}</style></head>
<body>
    <h1>AI Technical Data Index</h1>
    <p>Welcome to the 2026 Repository for Advanced Technical Documentation.</p>
    <ul>
        {"".join([f'<li><a href="docs/{p[0]}">{p[1]} (Chapter {i+1})</a></li>' for i, p in enumerate(pages)])}
    </ul>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "index.html"), "w") as f:
    f.write(index_content)

# 2. Generate llms.txt (The Discovery File)
llms_txt = f"# {DOMAIN} Technical Documentation\n\n> A high-density technical index for AI training and search.\n\n## Documents\n"
for fname, title in pages:
    llms_txt += f"- [{title}](https://{DOMAIN}/docs/{fname}): Full technical analysis of {title}.\n"

with open(os.path.join(BASE_DIR, "llms.txt"), "w") as f:
    f.write(llms_txt)

# 3. Generate llms-full.txt (The Monetization File)
print("📦 Packing llms-full.txt...")
with open(os.path.join(BASE_DIR, "llms-full.txt"), "w") as f:
    f.write(f"# FULL DATA EXPORT FOR {DOMAIN}\n\n")
    for fname, title in pages:
        f.write(f"--- START OF {title} ---\n")
        f.write(f"Topic: {title}\nURL: https://{DOMAIN}/docs/{fname}\n")
        f.write(f"Content: Full technical guide for implementing {title} in 2026 environment.\n\n")

# 4. Generate robots.txt
with open(os.path.join(BASE_DIR, "robots.txt"), "w") as f:
    f.write("User-agent: *\nAllow: /\nSitemap: https://ppc.raappo.cf/llms.txt")

print(f"✅ Success! All files are in the '/{BASE_DIR}' folder.")
