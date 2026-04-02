def analysis_prompt(raw_data):
  prompt = f"""Analyze this creator data:
  {raw_data}
  
  Return ONLY valid JSON:
  {{
    "niche_clarity": "...",
    "target_audience": "...",
    "monetization_gaps": ["...", "..."],....
    "digital_product_ideas": ["...", "..."],....
    }}
    """
  return prompt