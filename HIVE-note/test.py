from notes import save_note, load_note, convert_markdown_to_html


save_note("Test Note", "# This is a test\nThis note is saved in markdown format.")


content = load_note("Test Note")
print("Markdown Content:")
print(content)


html_content = convert_markdown_to_html(content)
print("\nConverted HTML:")
print(html_content)
