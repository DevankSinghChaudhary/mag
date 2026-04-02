def analysis_prompt(raw_data):
  if not raw_data:
    raise ValueError("No data for AI!")

  prompt = f"""Analyze this creator data:
  {raw_data}
  
  Return ONLY valid JSON:
  {{
    "niche_clarity": "...",
    "target_audience": "...",
    "monetization_gaps": ["...", "..."],
    "digital_product_ideas": ["...", "..."]
    }}
    """
  return prompt