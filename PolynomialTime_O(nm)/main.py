def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    if(all_handles and brand_name):
        for influencer in all_handles:
            for handle in influencer:
                if brand_name in handle:
                    count+=1
        num_influencer=len(all_handles)
        avg_brand_follower= count/num_influencer
        return avg_brand_follower
    return 0
