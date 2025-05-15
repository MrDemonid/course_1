# Разница времени и временных промежутков.

from datetime import timedelta


delta = timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5, milliseconds=6, microseconds=7)
print(f'{delta = }\t-\t{delta}')


delta = timedelta(weeks=53, days=500, hours=73, minutes=101, seconds=303, milliseconds=67890, microseconds=1234567)
neg_delta = timedelta(days=-3, minutes=-42)
print(f'{delta = }\t-\t{delta}')
print(f'{neg_delta = }\t-\t{neg_delta}')


# delta = datetime.timedelta(days=9, seconds=11045, microseconds=6007)	-	9 days, 3:04:05.006007

# delta = datetime.timedelta(days=874, seconds=10032, microseconds=124567)	-	874 days, 2:47:12.124567
# neg_delta = datetime.timedelta(days=-4, seconds=83880)	-	-4 days, 23:18:00
