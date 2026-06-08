from config_parser import config_file
from maze_generator import Maze
from exporter import MazeExporter

 
config = config_file("config.txt")
maze = Maze(config)
exporter = MazeExporter(maze)

print(exporter.to_ascii(), end="")
exporter.export_txt(config.OUTPUTFILE)
