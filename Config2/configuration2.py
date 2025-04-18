import pickle

config_dict = {
    "observation": {
        "type": "OccupancyGrid",
        "features": ['presence', 'on_road'],
        "grid_size": [[-18, 18], [-18, 18]],
        "grid_step": [3, 3],
        "as_image": False,
        "align_to_vehicle_axes": True
    },
    "action": {
        "type": "ContinuousAction",
        "longitudinal": False,
        "lateral": True
    },
    "simulation_frequency": 15,
    "policy_frequency": 5,
    "duration": 500,  # Augmenté pour permettre plus de temps d'exploration
    "collision_reward": -2.0,  # Pénalité plus forte pour collision
    "lane_centering_cost": 4,
    "action_reward": -0.3,
    "controlled_vehicles": 1,
    "other_vehicles": 1,
    "screen_width": 600,
    "screen_height": 600,
    "centering_position": [0.5, 0.5],
    "scaling": 7,
    "show_trajectories": False,
    "render_agent": True,
    "offscreen_rendering": True,
    "out_of_road_cost": -10,
    "terminal_on_out_of_road": True,
    "offroad_terminal": True,
    "reward_on_lane": 1.0,            
    "offroad_reward": -5.0,
    
    # Nouveaux paramètres pour favoriser les dépassements
    "reward_overtaking": 3.0,        # Forte récompense pour dépasser
    "high_speed_reward": 0.8,        # Augmenter récompense pour vitesse élevée
    "reward_speed_range": [25, 35],  # Plage de vitesse plus élevée
    "lane_change_reward": 0.1        # Légère récompense pour changement de voie
}

with open("config2.pkl", "wb") as f:
    pickle.dump(config_dict, f)

# env = gym.make("racetrack-v0")
# env.unwrapped.configure(config_dict)
# print(env.reset())