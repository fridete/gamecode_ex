# 功能：让管理员在生存模式下飞行
# 采用了python的数据段
# 有点漏，还可以
# 作者：骨亡
# 请和运行包一起装载，这是源码
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import mcpi.block as block
directions = (
    (0, 0, 0)
    (1, 0, 0)
    (1, 0, 1)
    (0, 0, 1)
    (-1, 0, 1)
    (-1, 0, 0)
    (-1, 0, -1)
    (0, 0, -1)
    (1, 0, -1)
)

mc = Minecraft.create()
created_block_positions = []

while True:
    position = mc.player.getTilePos() + Vec3(0, -1, 0)
    new_positions = []
    for direction in directions:
        new_positions = postion+Vec3(*direction)
        new_positions.append(new_position)
        block_type_id = mc.getBlock(new_positions)
        if block_type_id == block.AIR.id:
            mc.setBlock(new_position, block.GLASS)
            created_block_positions.append(new_position)

for created_created_block_position in created_block_positions:
    if created_block_position not in new_positions:
        mc.setBlock(created_block_position, block.AIR)
time.sleep(0.016
           )