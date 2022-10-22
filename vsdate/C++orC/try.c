#include <stdio.h>
void s_get();
//上面是字符串函数
int main()
{
    char result[40];
    //在循环前输入
    while (getchar() != "q")
    {
        int i;
        for (i = 0; i < 39; i++)
        {
            scanf("%s", result[i]);
            s_get(result[i]);
            printf(result[i]);
        }
    }
    system("pause"); //保证窗口不跳跃
    return 0;
}

void s_get(char word)
{
    if (word == "\n")
    {
        printf("error1:not a space");
    }
    if (word == "\0")
    {
        printf("error2:not a pointer");
    }
    if (word == NULL)
    {
        printf("error3:not a str");
    }
    if (word != "\n" && word != "\0" && word != NULL)
    {
        return word;
    }
}