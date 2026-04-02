from main import bio
from main import caption_l
from main import json_in
data = json_in(bio, caption_l)

prompt_analysis = f"""
Analyze this creator data:

{data}

Return ONLY valid JSON:

{{
  "niche_clarity": "...",
  "target_audience": "...",
  "monetization_gaps": ["...", "..."],
  "digital_product_ideas": ["...", "..."]
}}
"""