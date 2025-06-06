class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line


def vanity(influencer):
    vanity_score = (influencer.num_bio_links * 5) + influencer.num_selfies
    return vanity_score

def vanity_sort(influencers):
    influencers=sorted(influencers, key=vanity)
    return influencers
