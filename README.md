# NMS-patch-to-rating-analysis

A toy repo to see whether I can extract correlation between Hello Games [No Man's Sky](https://www.nomanssky.com/) patch releases and player ratings.

# Preliminary figures/results [^1]

> [!NOTE]
> The player review data presented herein have been extracted solely from [reviews of No Man's Sky submitted to the Steam marketplace](https://store.steampowered.com/app/275850/No_Mans_Sky/). These data may not be representative of the entire population of players, and I would emphasise that caution must be taken in interpreting or extrapolating the results presented here.

In the following, I make use of a player review score metric, which is expressed as a percentage and which I have defined as the cumulative total of positive (i.e. "up vote") reviews over the total number of reviews (positive and negative) as a function of time.

!['NMS review score and major releases timeline'](https://github.com/ATHannington/NMS-patch-to-rating-analysis/blob/main/Figures/NMS-review-score-vs-time_major-releases.jpg?v_30-07-2025|Major-release-timeline)

Here we can see the general trend of player reviews left on Steam as a function of time since NMS was first released in 2016. Overlaid in vertical red lines are the dates of major releases/updates to NMS. We can already see some signs of an almost step-function-like increase in player reviews before major updates are released.

!['NMS review score and timeline of all major and minor releases'](https://github.com/ATHannington/NMS-patch-to-rating-analysis/blob/main/Figures/NMS-review-score-vs-time_all-releases.jpg?v_30-07-2025|All-releases-timeline)

Now, bringing in the bug fix releases as blue vertical lines, we start to see the influence of the groups of minor, bug-fixing updates that follow a major update. A qualitative assessment of these figures suggests a positive correlation between game updates (including both major patch releases and minor bug fixes) and the overall player review score.

> [!NOTE]
> The player review score presented in this analysis will be subject to low-number statistics at early times. Therefore, I will try to update this page soon with a total review count versus time graph, which will aid in interpreting the player review score.

!['NMS review dataset cross correlation heatmap'](https://github.com/ATHannington/NMS-patch-to-rating-analysis/blob/main/Figures/NMS-review-data-cross-correlation-matrix-heatmap.jpg?v_30-07-2025|Review-dataset-cross-correlation-heatmap)

This figure shows a cross-correlation heatmap between different features in the Steam review dataset. This matrix shows the correlation between each of the different features :

1.   num_games_owned              -  int64         
2.   num_reviews                  -  int64         
3.   playtime_forever             -  int64         
4.   playtime_last_two_weeks      -  int64         
5.   playtime_at_review           -  float64       
6.   last_played                  -  int64         
7.   _**Date**_ (timestamp_created)            -  datetime64[ns]
8.   timestamp_updated            -  datetime64[ns]
9.   _**voted_up**_                     -  bool          
10.  votes_up                     -  int64         
11.  votes_funny                  -  int64         
12.  weighted_vote_score          -  float64       
13.  comment_count                -  int64         
14.  steam_purchase               -  bool          
15.  received_for_free            -  bool          
16.  written_during_early_access  -  bool          
17.  primarily_steam_deck         -  bool 

For the documentation summarising these different data features, I refer the reader to ["The unofficial and internal Steam Web API" by Revadike](https://github.com/Revadike/InternalSteamWebAPI) and the documentation provided for the API tool [Get-App-Reviews](https://github.com/Revadike/InternalSteamWebAPI/wiki/Get-App-Reviews).

In the above list, I have _**highlighted**_ the two key variables we are interested in. _**voted_up**_ indicates whether a review was favourable or not, and _**Date**_ (an alias for ["timestamp_created"](https://github.com/Revadike/InternalSteamWebAPI/wiki/Get-App-Reviews)) provides the date the review was initially written.

Focussing on our target variable of interest, "upvote_perc" (i.e. the player review score, expressed in percentage), there appears to be a positive correlation between upvote percentage and timestamp of review. This probably reflects the influence of increasingly favourable reviews with time, as well as the small number statistics at the earliest dates in our dataset, immediately following the game's release. We may need to account for this latter effect, possibly by using methods which decrease the weighted influence of older reviews.

On an individual basis (which is the main insight we can derive from this non-aggregated, near-to-being-completely-raw dataset), we can see correlation between a favourable review on an individual level also correlates with the date of the review. This may be due to the aforementioned influence of increasing percentage of favourable reviews with time, influence of large (low) number statistics at present-day (older) dates, and an increase in player numbers as the upvote percentage increases and new players decide to try the game as a result. Playtime at review and playtime forever also show positive correlation with upvote percentage, showing gamers who review it favourably are likely to played it longer before reviewing it, and to play it more overall (before and after the review) - which is to be expected. 

Players who purchased the game through Steam are less likely to leave a favourable review, but care needs to be taken when interpretting this aspect of the data as their is inherent bias introduced on this measure by the fact that the reviews have solely been sourced from Steam.

[^1]: The information provided on this page and within the contents of this repository is for general informational purposes only.
