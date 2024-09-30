from modules.gpt import *
from modules.spotify import *
from modules.control import *
from modules.tts import *

tools = [
    {
        "type": "function",
        "function": {
            "name": "write_text",
            "description": "Writes the text given in the to the computer, use only if you must.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The text to be written."
                    }
                },
                "required": ["text"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "shutdown_pc",
            "description": "Shuts down the computer in 'when' seconds.",
            "parameters": {
                "type": "object",
                "properties": {
                    "when": {
                        "type": "string",
                        "description": "Seconds until the shutdown."
                    },
                    "restart": {
                        "type": "boolean",
                        "description": "True for restart, False for shutdown."
                    }
                },
                "required": ["when", "restart"],
                "additionalProperties": False
            }
        }
    },

    {
       "type": "function",
       "function": {
           "name": "click_coord",
           "description": "Clicks a coordinate.",
           "parameters": {
               "type": "object",
               "properties": {
                   "x": {
                       "type": "integer",
                       "description": "X coordinate."
                   },
                   "y": {
                       "type": "integer",
                       "description": "Y coordinate."
                   },
                   "right": {
                       "type": "boolean",
                       "description": "right click?",
                       "default": False
                   },
               },
               "required": ["x", "y"],
               "additionalProperties": False
           }
       }
   },
   {
       "type": "function",
       "function": {
           "name": "read_notes",
           "description": "Reads the notes file for additional information you have written down, read if you dont know something.",
       }
   },
   {
       "type": "function",
       "function": {
           "name": "write_to_notes",
           "description": "If you wish to write down extra information to remember for the next time. ",
           "parameters": {
               "type": "object",
               "properties": {
                   "text": {
                       "type": "string",
                       "description": "The text to put in the notes file. Make sure its a token efficient text."
                   },
               },
               "required": ["text"],
               "additionalProperties": False
           }
       }
   },
   {
       "type": "function",
       "function": {
           "name": "play_song",
           "description": "Plays selected song on Spotify.",
           "parameters": {
               "type": "object",
               "properties": {
                   "song_name": {
                       "type": "string",
                       "description": "The title of the song."
                   },
                   "artist_name":{
                       "type": "string",
                       "description": "The name of the artist, only if you are sure about it.",
                       "default": False
                   }
               },
               "required": ["song_name"],
               "additionalProperties": False
           }
       }
   },
   {
       "type": "function",
       "function": {
           "name": "add_song_to_queue",
           "description": "Adds selected song to the Spotify queue to be played.",
           "parameters": {
               "type": "object",
               "properties": {
                   "song_name": {
                       "type": "string",
                       "description": "The title of the song."
                   },
                   "artist_name":{
                       "type": "string",
                       "description": "The name of the artist, only if you are sure about it.",
                       "default": False
                   }
               },
               "required": ["song_name"],
               "additionalProperties": False
           }
       }
   },
   {
       "type": "function",
       "function": {
           "name": "run_system_command",
           "description": "Run any Windows CMD command. ",
           "parameters": {
               "type": "object",
               "properties": {
                   "command": {
                       "type": "string",
                       "description": "Command to run, use the format you would use in a Windows CMD command."
                   },
                   "return_message":{
                       "type": "string",
                       "description": "If you would like to call another function, or say something, put that here.",
                       "default": None
                   }
               },
                   
               "required": ["command"],
               "additionalProperties": False
           }
       }
   },
   {
       "type": "function",
       "function": {
           "name": "create_file",
           "description": "Creates a file using the echo command.",
           "parameters": {
               "type": "object",
               "properties": {
                   "path": {
                       "type": "string",
                       "description": "The path to where the file should be created along with the file name and extension."
                   },
                   "content": {
                       "type": "string",
                       "description": "The content of the file."
                   },
               },
               "required": ["path", "content"],
               "additionalProperties": False
           }
       }
   },
    
]