        
# Ditch YouTube API (BETA)          
 **DYA** ( *Ditch YouTube API* ) is a package created to power the user with YouTube Data API functionality **without any API Key**.       
   
  *Currently, on development! More methods will be added soon.*     
    
 **GitHub [Repository](https://github.com/jnsougata/Ditch-YouTube-API)**               
 # How to use?   
 - **Installation:** - `pip install dya`          
 - **Importing DYA:** - `from DYA import Search, Video, Channel`          
          
 - **Creating an instance of target YouTube Channel:**    
- `channel = Channel("Channel ID/ Custom ID/ URL/ CustomURL") `     
 - **Attributes:** 
 - `live`
 > Returns ***True*** if channel is Live at that moment, Otherwise returns ***False***          
 - `stream_link` 
 > Returns ***URL*** of Livestream if channel is Live at that moment, otherwise returns ***None***          
 - `latest_uploads(*limit)` 
 > Returns ***List*** of Latest Uploaded **Video ID** if channel is not live at that moment, otherwise returns ***None***  
  
- `info`   
> Returns a **Dict** of the **About** of the YouTube Channel. Dict contains channel ***Name***, ***Subscribers***, ***Description***, ***TotalViews***, ***JoiningDate***, ***Country***, ***CustomURL***  , ***Channel Avatar Banner***,  ***Channel Banner URL***

 - `playlists` 
 > Returns a List containing ordered paired **[ Name, ID ]** of public playlists' ***List***    
    
- Or, you can use **independent attributes** to get channel info:    
    
	 - `name` Returns **Name** of the channel or **None**     
	- `subs` Returns **Sub-count** of the channel or **None**  
	- `total_views` Returns total number of **Views** of the channel or **None**     
	- `joined_at` Returns channel **creation date** or **None** 
	- `country` Returns the generic country of the channel or **None**
   - `custom_url` Returns the **Custom URL** of the channel or **None** 
   - `description` Returns the **Description** of the channel or **None** 
   - `avatar_url` Returns the **Avatar URL** of the channel or **None** 
   - `banner_url` Returns the **Banner URL** of the channel or **None**
   
- **Creating an instance of YouTube Search:**    
	- `Query = Search(*keywords: str)`    
    
  - ***Getting videos by query:*** 
	  - `Result = Query.get_video`    
		> Returns a **Video ID** according to queries.
		   
	- `Results = Query.get_videos(*limit: int[optional])`    
		> Returns a list of **VideoIDs** according to queries.   
		     
  - ***Getting channels by query:***    
	- `Result = Query.get_channel`    
		> Returns a **Channel ID** according to queries.
		
	- `Results = Query.get_channels(*limit: int[optional])`    
		> Returns a list of **Channel IDs** according to queries.        
    
 - **Creating an instance of Video Data:**    
- `vid = Video("Video ID")`    
 - **Attributes:**    
- `info` 
> Returns a **Dict** of video information [ **title**, **views**, **likes**, **dislikes**, **channel_id, duration**, **upload_date**, **thumbnail**, **tags** ]

- Or, you can use **independent attributes** to get each info individually:    
	 - `title` -- Returns **title** of the video    
   - `views` -- Returns **view count** of the video    
   - `likes` -- Returns total **likes** on the video    
   - `dislikes` -- Returns total **dislikes** on the video    
   - `channel_id` -- Returns **channel id** from which the video belong    
   - `duration` -- Returns **duration** of the video    
   - `upload_date` -- Returns **date of upload** of the video    
   - `description` -- Returns whole **description** of the video    
   - `tags` -- Returns **list of tags** of the video    
   - `thumbnail` -- Returns **HQ Thumbnail** of the video
