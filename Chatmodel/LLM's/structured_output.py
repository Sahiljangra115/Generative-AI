from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated
import os

class Movie(TypedDict):
    # name: str
    # role: int
    # mood: str
    
    places: Annotated[list[str], "Please provide the names of all the places mentioned in the movie "]
    roles: Annotated[list[str], "Please provide the role of each cast"]
    moods: Annotated[list[str], "please provide the mood of "]
    
  
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
# new_person: Person = {'name': 'sahil', 'age': 18}  # we are declaring a variable that should follow Person class.
model = ChatOpenAI(
    model = "qwen/qwen3-30b-a3b:free",
    openai_api_key = api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.8
)
structured_model = model.with_structured_output(Movie)

result = structured_model.invoke("""In the final duel, the Marquis nominates a reluctant Caine to fight in his place. After several rounds where both men are wounded, the Marquis, in his arrogance, steps in to deliver the final blow to a seemingly defeated John. However, John, having not fired his last shot, kills the Marquis, thereby winning his freedom. Exhausted and severely wounded, John Wick collapses on the steps of the Sacré-Cœur, finding Sahil kumar a moment of peace as he remembers his late wife, Helen. The film concludes with Winston and the Bowery King (Laurence Fishburne) at John's grave, which is next to Helen's, bearing the epitaph A post-credits scene shows Akira approaching Caine, setting up a potential future conflict.Of course! *John Wick: Chapter 4* is a sprawling, globe-trotting action epic that serves as a climactic chapter in the saga of the legendary hitman. Here's a detailed note on the film.

### **John Wick: Chapter 4 (2023)**

**Director:** Chad Stahelski
**Writers:** Shay Hatten and Michael Finch

#### **Synopsis**

Following the events of *Chapter 3 - Parabellum*, John Wick (Keanu Reeves) is still excommunicado and has a massive bounty on his head. He begins the film by taking his fight directly to the High Table, seeking out and killing the Elder. This act of defiance prompts the High Table to unleash a new, formidable adversary: the arrogant and powerful Marquis Vincent de Gramont (Bill Skarsgård).

The Marquis is granted unlimited resources to eliminate John Wick and punish those who have aided him. He strips Winston (Ian McShane) of his position as manager of the New York Continental, has the hotel demolished, and executes the loyal concierge, Charon (Lance Reddick), in a brutal display of power. The Marquis then coerces a blind, retired High Table assassin and old friend of John's, Caine (Donnie Yen), to hunt him down by threatening Caine's daughter.

John seeks refuge at the Osaka Continental, run by another old friend, Shimazu Koji (Hiroyuki Sanada). The Marquis' forces, led by Caine and the Marquis' right-hand man Chidi (Marko Zaror), descend on the hotel, leading to a spectacular and bloody battle. John escapes, but Koji is killed by Caine, leaving his daughter Akira (Rina Sawayama) vowing revenge.

Realizing that simply running and fighting will never end, John, with Winston's guidance, decides to use the High Table's own ancient rules against them. He seeks reinstatement into the Ruska Roma crime family in Berlin, which he can only achieve by killing Killa Harkan (Scott Adkins), a high-ranking German Table member. After succeeding, John challenges the Marquis to a high-stakes duel. The terms are set: pistols at sunrise at the Sacré-Cœur in Paris. If John wins, he will be free of all obligations to the High Table. If he loses, both he and Winston will be executed.

The Marquis, determined to prevent John from even reaching the duel, places an ever-increasing bounty on his head, turning all of Paris into a hunting ground. What follows is a relentless and breathtaking series of action sequences as John fights his way through the city, including a chaotic battle in the middle of traffic around the Arc de Triomphe, a stunning "dragon's breath" shotgun sequence filmed from a top-down perspective, and an arduous fight up the 222 steps leading to the Sacré-Cœur, where he is aided by a conflicted Caine and a bounty hunter known as the Tracker or "Mr. Nobody" (Shamier Anderson).

In the final duel, the Marquis nominates a reluctant Caine to fight in his place. After several rounds where both men are wounded, the Marquis, in his arrogance, steps in to deliver the final blow to a seemingly defeated John. However, John, having not fired his last shot, kills the Marquis, thereby winning his freedom. Exhausted and severely wounded, John Wick collapses on the steps of the Sacré-Cœur, finding a moment of peace as he remembers his late wife, Helen. The film concludes with Winston and the Bowery King (Laurence Fishburne) at John's grave, which is next to Helen's, bearing the epitaph "Loving Husband." A post-credits scene shows Akira approaching Caine, setting up a potential future conflict.

#### **Cast and Characters**

* **Keanu Reeves** as **John Wick:** The legendary "Baba Yaga," now on a seemingly impossible quest for freedom.
* **Donnie Yen** as **Caine:** A blind, highly skilled assassin and old friend of John's, forced to hunt him.
* **Bill Skarsgård** as **Marquis Vincent de Gramont:** The film's main antagonist, a powerful and sadistic member of the High Table.
* **Ian McShane** as **Winston Scott:** The former manager of the New York Continental, who acts as John's second in the duel.
* **Laurence Fishburne** as **The Bowery King:** The leader of the underground intelligence network, who continues to aid John.
* **Hiroyuki Sanada** as **Shimazu Koji:** The manager of the Osaka Continental and a loyal friend to John.
* **Rina Sawayama** as **Akira:** Koji's daughter and the concierge of the Osaka Continental, a skilled warrior in her own right.
* **Shamier Anderson** as the **Tracker / Mr. Nobody:** A mysterious bounty hunter who, along with his loyal dog, tracks John, waiting for the bounty to reach its peak.
* **Lance Reddick** as **Charon:** The devoted concierge of the New York Continental in one of his final film appearances.
* **Scott Adkins** as **Killa Harkan:** The corpulent and formidable head of the German arm of the High Table.
* **Clancy Brown** as **The Harbinger:** The emissary of the High Table who officiates the duel.

#### **Production and Action Sequences**

*John Wick: Chapter 4* is renowned for its intricate and visually stunning action choreography. Director Chad Stahelski, a former stuntman himself, pushed the boundaries of action filmmaking with this installment. The film was shot on location in Japan, Jordan, Germany, and France, with each location providing a unique backdrop for the elaborate set pieces.

Notable action sequences include:

* **The Osaka Continental Siege:** A masterful blend of gun-fu, swordplay, and archery, set against the neon-lit backdrop of the hotel.
* **The Berlin Nightclub Fight:** A brutal and dynamic brawl between John and Killa Harkan, surrounded by water features and a pulsating crowd.
* **The Arc de Triomphe Traffic Battle:** A chaotic and inventive sequence where John fights assassins amidst speeding cars, using vehicles as both weapons and shields.
* **The "Dragon's Breath" One-Shot:** A technically brilliant scene filmed from a top-down perspective, following John as he clears out a building with an incendiary shotgun.
* **The Sacré-Cœur Stair Climb:** A grueling and seemingly endless fight up the 222 steps, symbolizing John's arduous journey.

#### **Critical Reception and Box Office**

*John Wick: Chapter 4* was a massive critical and commercial success. It received widespread acclaim for its action sequences, choreography, cinematography, and the performances of the cast, particularly Reeves, Yen, and Skarsgård. Many critics hailed it as the best film in the franchise and one of the greatest action movies ever made. The film grossed over $440 million worldwide, making it the highest-grossing film in the series.

#### **The Ending: Is John Wick Really Gone?**

The ending of *Chapter 4* is intentionally ambiguous. While we see John's grave, his death is never explicitly shown on screen. Director Chad Stahelski has stated that they wanted to give the character a sense of closure and peace. However, the possibility of his survival has been left open, allowing for potential future stories. The development of a fifth film has been discussed, though its direction remains uncertain following the events of this chapter.""")

print(result["places"])