from .. import GraiaMiraiApplication, get
from ..command import group_commands, friend_commands
from ..message import MessageChain, Group, Member, Friend


bcc = get.bcc()
__plugin_name__ = "指令处理器"
__plugin_usage__ = """功能暂未写完。因此没有实际作用"""


@bcc.receiver("GroupMessage")
async def Group_instruction_processor(
    bot: GraiaMiraiApplication,
    msesage: MessageChain,
    group: Group, member: Member
):
    for k, v in group_commands.items():
        if msesage.asDisplay() == k:
            v()


@bcc.receiver("FriendMessage")
async def f_instruction_processor(
    bot: GraiaMiraiApplication,
    msesage: MessageChain,
    friend: Friend, member: Member
):
    for k, v in friend_commands.items():
        if msesage.asDisplay() == k:
            v()
