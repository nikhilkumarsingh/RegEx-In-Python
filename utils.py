import re
from colorama import Back, Style


def highlight_regex_matches(pattern, text, print_output=True):
	output = text
	len_inc = 0
	for match in pattern.finditer(text):
		start, end = match.start() + len_inc, match.end() + len_inc
		output = output[:start] + Back.YELLOW + Style.BRIGHT + output[start:end] + Style.RESET_ALL + output[end:]
		len_inc = len(output) - len(text)  

	if print_output:
		print(output)
	else:
		return output
