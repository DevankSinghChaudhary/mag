def audit_prompt(json_output):
  prompt = f"""Analyze this creator data:
  {json_output}
  
  Return ONLY valid JSON:
  {{
    "niche_clarity": "...",
    "target_audience": "...",
    "monetization_gaps": ["...", "..."],....
    "digital_product_ideas": ["...", "..."],....
    }}
    """
  return prompt