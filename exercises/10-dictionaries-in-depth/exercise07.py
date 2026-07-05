# Exercise 7: Config Merge
# Merge multiple config dicts with | and |= operators.

default_config = {"theme": "light", "font_size": 12, "show_sidebar": True, "language": "en"}
user_config = {"theme": "dark", "font_size": 14, "language": "fr"}
env_config = {"font_size": 16}

# Merge with | (env > user > default)
final = default_config | user_config | env_config
print(f"Merged: {final}")

# Step by step with |=
config = {}
config |= default_config
print(f"After defaults: {config}")
config |= user_config
print(f"After user: {config}")
config |= env_config
print(f"After env: {config}")

# Compare with .update()
config2 = {}
config2.update(default_config)
config2.update(user_config)
config2.update(env_config)
print(f"update() produces the same result: {config == config2}")
