
def sum_from_text(message_text):
	nums = [int(s) for s in message_text.split() if s.isdigit()]
	answer = 0
	i = 0
	while i < len(nums):
		answer += nums[i]
		i += 1
	return answer

