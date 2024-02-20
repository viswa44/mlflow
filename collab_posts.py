import numpy as np

class CollaborativeFilteringPosts:
    def __init__(self, user_post_matrix):
        self.user_post_matrix = np.array(user_post_matrix)

    def find_similar_users(self, user_id, num_users=5):
        """
        Finds similar users to the given user based on their interactions with posts.
        """
        similarities = {}
        for other_user_id in range(len(self.user_post_matrix)):
            if other_user_id != user_id:
                similarity = self.calculate_similarity(user_id, other_user_id)
                similarities[other_user_id] = similarity

        similar_users = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        return similar_users[:num_users]

    def calculate_similarity(self, user1_id, user2_id):
        """
        Calculates similarity between two users based on their interactions with posts.
        """
        user1_vector = self.user_post_matrix[user1_id]
        user2_vector = self.user_post_matrix[user2_id]

        # Using cosine similarity
        dot_product = np.dot(user1_vector, user2_vector)
        magnitude_user1 = np.linalg.norm(user1_vector)
        magnitude_user2 = np.linalg.norm(user2_vector)

        if magnitude_user1 == 0 or magnitude_user2 == 0:
            return 0  # If one of the users has no interactions, similarity is 0.

        return dot_product / (magnitude_user1 * magnitude_user2)

    def recommend_posts(self, user_id, num_recommendations=5):
        """
        Recommends posts to the given user based on similar users' interactions.
        """
        similar_users = self.find_similar_users(user_id)
        recommendations = []

        for other_user_id, similarity in similar_users:
            other_user_vector = self.user_post_matrix[other_user_id]
            for post_id, interaction in enumerate(other_user_vector):
                if interaction == 1 and self.user_post_matrix[user_id][post_id] == 0:
                    recommendations.append(post_id)

            if len(recommendations) >= num_recommendations:
                break

        return recommendations

# Example usage:
user_post_matrix = [
    [1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 1]
]

cf_posts = CollaborativeFilteringPosts(user_post_matrix)
user_id = 0
recommendations = cf_posts.recommend_posts(user_id)
print("Recommendations for user", user_id, ":", recommendations)


### recommends posts based on user item interaction
