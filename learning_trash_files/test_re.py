import re

re_uuid = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}$', re.I)

uuid_pattern = '[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}'

re_asctime = re.compile('^[0-9]{4}-[0-1][0-9]-[0-3][0-9] [0-2][0-9]:[0-6][0-9]:[0-6][0-9],[0-9]{3} - INFO - UUID: ' + uuid_pattern + ' - X-Flag: green$', re.I)

line = "2024-07-20 19:37:59,423 - INFO - UUID: fe5d74c5-e5cd-49e5-83ad-712edc52ae7d - X-Flag: green"

# is_match = re_asctime.match(line).group(0)
# print(is_match)
# print(is_match[-5:])


uuid_pattern2 = '[^"]*[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}[^"]*'
# uuid_pattern2 = '[^"]*[a-f0-9]{12}[^"]*'

re_uuid_pattern = re.compile(uuid_pattern2, re.I)

iss_match = re_uuid_pattern.match(line)
if iss_match:
	print(iss_match)
