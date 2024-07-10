from pypresence import Presence
import time

client_id = "1207798378029912124" # replace with your bot client id
RPC = Presence(client_id)
RPC.connect()
time_now = int(time.time())

def set_activity(timer):
    RPC.update(
        details="Hacking:",
        state="In Progress (3/5)",
        start=time_now, # You can remove this if you don't need time elapsed
        # end = time_now+86400,
        end=None,
        large_image="neo",  # Upload image with this exact name(In my case neo.png) to discord bot rich presence Art section
        large_text="I use white theme in discord btw",
        small_image=None,
        small_text=None,
        party_id=None, # don't need any of these actually 
        party_size=None,
        join=None,
        spectate=None,
        match=None,
        buttons=[ # Buttons are visible only with discord nitro, sad :(
            {
                "label": "Stop Hacking",
                "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            },
            {
                "label": "Continue Hacking",
                "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            },
        ],
        instance=True,
        payload_override=None,
    )


timer = 1
while True:
    set_activity(timer) 
    time.sleep(1)   # this for any animations in your presence, keep it 1 second or expect lags from discord
    timer += 1
