# CS514L-CS22B046_CS22B059
## Assignment-2



### 🛠️ Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/Mokshith1708/CS514L-CS22B046_CS22B059
cd CS514L-CS22B046_CS22B059

```
#### 2. Install Dependencies
``` bash
pip install -r requirements.txt
```

### 3. To Run BnB algorithm:
``` bash
cd Frozen_lake\BnB
python wrapper.py  # for running the code

python gif_generation.py # for generating gif.
```

### 3. To Run IDA* algorithm:
``` bash
cd Frozen_lake\IDA
python wrapper.py  # for running the code

python gif_generation.py # for generating gif.
```

### Note: For running hill climging and simulated annealing we need the environment for that We used this repo:
url: https://github.com/kevin-schumann/VRP-GYM

### 4. Steps to setup the environment:
``` bash
cd TSP
git clone https://github.com/kevin-schumann/VRP-GYM.git
cd VRP-GYM
```
   - Now open the VRP-GYM/setup.py file.
   - Find this line (or similar):
        packages=find_packages()
   - Change it to this:
        packages=find_packages(include=["gym_vrp", "gym_vrp.*"]),

   - now run this command:

``` bash
pip install -e .
```

### 3. To Run Hill Climbing (steepest ascent) algorithm:
``` bash
cd TSP/Hill_Climbing
python wrapper.py  # for running the code and gif generation
```

### 3. To Run Simulated Annealing (steepest ascent) algorithm:
``` bash
cd TSP/Hill_Climbing
python wrapper.py  # for running the code and gif generation
```