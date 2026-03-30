

from app.queries import *

print(get_all_subscriptions(1))
print(get_dead_subscriptions(1))
print(get_monthly_trend(1))
print("Health Score:", get_health_score(1))

