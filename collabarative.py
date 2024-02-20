class CollaborativeFiltering:
    def __init__(self, user_item_matrix):
        self.user_item_matrix = user_item_matrix

    def find_similar_users(self, user_id, num_users=5):
        """
        Finds similar users to the given user based on user-item interactions.
        """
        # Calculate similarities between the given user and all other users
        similarities = {}
        for other_user_id in range(len(self.user_item_matrix)):
            if other_user_id != user_id:
                similarity = self.calculate_similarity(user_id, other_user_id)
                similarities[other_user_id] = similarity

        # Sort users based on similarity
        similar_users = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

        # Return top N similar users
        return similar_users[:num_users]

    def calculate_similarity(self, user1_id, user2_id):
        """
        Calculates similarity between two users based on their interactions.
        Here, we use cosine similarity.
        """
        user1_vector = self.user_item_matrix[user1_id]
        user2_vector = self.user_item_matrix[user2_id]

        dot_product = sum(user1_vector[i] * user2_vector[i] for i in range(len(user1_vector)))
        magnitude_user1 = sum(val ** 2 for val in user1_vector) ** 0.5
        magnitude_user2 = sum(val ** 2 for val in user2_vector) ** 0.5

        if magnitude_user1 == 0 or magnitude_user2 == 0:
            return 0  # If one of the users has no interactions, similarity is 0.

        return dot_product / (magnitude_user1 * magnitude_user2)

    def recommend_users(self, user_id, num_recommendations=5):
        """
        Recommends users to the given user based on similar users' preferences.
        """
        similar_users = self.find_similar_users(user_id)
        recommendations = []

        for other_user_id, similarity in similar_users:
            other_user_vector = self.user_item_matrix[other_user_id]
            for i, value in enumerate(other_user_vector):
                if value == 1 and self.user_item_matrix[user_id][i] == 0:  # User hasn't interacted with this item
                    recommendations.append(i)

            if len(recommendations) >= num_recommendations:
                break

        return recommendations

# Example usage:
user_item_matrix = [
    [1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 1]
]

cf = CollaborativeFiltering(user_item_matrix)
user_id = 0
recommendations = cf.recommend_users(user_id)
print("Recommendations for user", user_id, ":", recommendations)



#this suggests only profiles <<---------------
#based on user-item interaction 